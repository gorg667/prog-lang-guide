/* Client-side behaviour for the guide site. No dependencies. */
(function () {
  'use strict';

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  /* ---------- Theme ---------- */
  const themeBtn = $('#themeBtn');
  themeBtn.addEventListener('click', () => {
    const dark = document.documentElement.classList.toggle('dark');
    try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) { /* ignore */ }
  });

  /* ---------- Mobile nav ---------- */
  const menuBtn = $('#menuBtn');
  const scrim = $('#scrim');
  const setNav = (open) => {
    document.body.classList.toggle('nav-open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
  };
  menuBtn.addEventListener('click', () => setNav(!document.body.classList.contains('nav-open')));
  scrim.addEventListener('click', () => setNav(false));
  $('#toc').addEventListener('click', (e) => { if (e.target.closest('a')) setNav(false); });

  /* ---------- Wrap tables for horizontal scroll; colorize star ratings ---------- */
  $$('.prose table').forEach((t) => {
    if (t.parentElement.classList.contains('table-wrap')) return;
    const w = document.createElement('div');
    w.className = 'table-wrap';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });
  $$('.prose td').forEach((td) => {
    if (/^★{1,5}/.test(td.textContent.trim())) {
      td.innerHTML = td.innerHTML.replace(/(★+)/, '<span class="stars">$1</span>');
    }
  });

  /* ---------- Reading progress + back to top ---------- */
  const progress = $('#progress');
  const toTop = $('#toTop');
  const onScroll = () => {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    progress.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    toTop.hidden = h.scrollTop < 600;
  };
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- Scroll-spy for sidebar ---------- */
  const tocLinks = $$('#toc a');
  const byId = new Map(tocLinks.map((a) => [a.dataset.target, a]));
  const headings = $$('.prose h2, .prose h3').filter((h) => byId.has(h.id));
  let active = null;
  const setActive = (id) => {
    if (active === id) return;
    active = id;
    tocLinks.forEach((a) => a.classList.toggle('active', a.dataset.target === id));
    const a = byId.get(id);
    if (a) {
      const sb = $('#sidebar');
      const r = a.getBoundingClientRect();
      const sr = sb.getBoundingClientRect();
      if (r.top < sr.top + 40 || r.bottom > sr.bottom - 40) a.scrollIntoView({ block: 'center' });
    }
  };
  if ('IntersectionObserver' in window && headings.length) {
    const visible = new Set();
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => (en.isIntersecting ? visible.add(en.target) : visible.delete(en.target)));
      // Choose the top-most visible heading; if none, the last heading above viewport.
      let pick = null;
      if (visible.size) {
        pick = Array.from(visible).sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0];
      } else {
        const top = 70;
        for (const h of headings) if (h.getBoundingClientRect().top < top) pick = h;
      }
      if (pick) setActive(pick.id);
    }, { rootMargin: '-60px 0px -70% 0px', threshold: 0 });
    headings.forEach((h) => io.observe(h));
  }

  /* ---------- Search ---------- */
  let index = [];
  try { index = JSON.parse($('#searchIndex').textContent); } catch (e) { index = []; }
  // Precompute lowercase fields and breadcrumb (nearest level-2 ancestor).
  let lastL2 = '';
  index.forEach((s) => {
    if (s.l <= 2) lastL2 = s.t;
    s.crumb = s.l > 2 ? lastL2 : '';
    s.tl = s.t.toLowerCase();
    s.bl = s.b.toLowerCase();
  });

  const input = $('#searchInput');
  const results = $('#searchResults');
  let cursor = -1;

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const hl = (text, terms) => {
    let out = esc(text);
    terms.forEach((t) => {
      const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
      out = out.replace(re, '<mark>$1</mark>');
    });
    return out;
  };
  const snippet = (body, terms) => {
    const bl = body.toLowerCase();
    let pos = -1;
    for (const t of terms) { pos = bl.indexOf(t); if (pos >= 0) break; }
    if (pos < 0) return body.slice(0, 140) + (body.length > 140 ? '…' : '');
    const start = Math.max(0, pos - 60);
    const end = Math.min(body.length, pos + 110);
    return (start > 0 ? '…' : '') + body.slice(start, end) + (end < body.length ? '…' : '');
  };

  const search = (q) => {
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    const scored = [];
    for (const s of index) {
      let score = 0;
      let all = true;
      for (const t of terms) {
        const inTitle = s.tl.includes(t);
        const inBody = s.bl.includes(t);
        if (!inTitle && !inBody) { all = false; break; }
        score += inTitle ? 10 : 0;
        score += inBody ? 1 : 0;
        if (s.tl.startsWith(t)) score += 5;
      }
      if (all) {
        if (s.l === 2) score += 2;
        scored.push({ s, score });
      }
    }
    scored.sort((a, b) => b.score - a.score);
    return scored.slice(0, 12).map((x) => x.s);
  };

  const render = (q) => {
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    const hits = search(q);
    cursor = -1;
    if (!q.trim()) { results.hidden = true; results.innerHTML = ''; return; }
    if (!hits.length) {
      results.innerHTML = '<div class="empty">No matches for “' + esc(q) + '”.</div>';
      results.hidden = false;
      return;
    }
    results.innerHTML = hits.map((s) =>
      '<a href="#' + s.s + '" role="option">' +
      (s.crumb ? '<div class="r-crumb">' + esc(s.crumb) + '</div>' : '') +
      '<div class="r-title">' + hl(s.t, terms) + '</div>' +
      '<div class="r-snip">' + hl(snippet(s.b, terms), terms) + '</div>' +
      '</a>'
    ).join('');
    results.hidden = false;
  };

  const close = () => { results.hidden = true; };
  const moveCursor = (d) => {
    const items = $$('a', results);
    if (!items.length) return;
    cursor = (cursor + d + items.length) % items.length;
    items.forEach((a, i) => a.classList.toggle('active', i === cursor));
    items[cursor].scrollIntoView({ block: 'nearest' });
  };

  let t;
  input.addEventListener('input', () => { clearTimeout(t); t = setTimeout(() => render(input.value), 80); });
  input.addEventListener('focus', () => { if (input.value.trim()) render(input.value); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); moveCursor(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); moveCursor(-1); }
    else if (e.key === 'Enter') {
      const items = $$('a', results);
      const target = items[cursor >= 0 ? cursor : 0];
      if (target) { location.hash = target.getAttribute('href'); close(); input.blur(); }
    } else if (e.key === 'Escape') { close(); input.blur(); }
  });
  results.addEventListener('click', (e) => { if (e.target.closest('a')) { close(); input.blur(); } });
  document.addEventListener('click', (e) => { if (!e.target.closest('.search')) close(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && !/input|textarea|select/i.test(document.activeElement.tagName)) {
      e.preventDefault(); input.focus(); input.select();
    }
  });

  /* ---------- External links open in new tab ---------- */
  $$('.prose a[href^="http"]').forEach((a) => { a.target = '_blank'; a.rel = 'noopener'; });
})();
