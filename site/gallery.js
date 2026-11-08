'use strict';

const catalog = window.AI_FUN_CATALOG;
const $ = id => document.getElementById(id);
const copy = {
  skip: ['跳到作品列表', 'Skip to the gallery'],
  headline: ['小游戏、3D 世界，还有些怪点子', 'Games, worlds & odd experiments'],
  intro: ['收集大家用 AI 做出来的作品，附原始演示、试玩和作者出处。', 'Things people make with AI, with original videos, demos and credits.'],
  gallery: ['全部作品', 'All works'],
  searchLabel: ['搜索作品', 'Search works'],
  searchHint: ['搜索作品', 'Search works'],
  playable: ['只看可试玩', 'Playable only'],
  empty: ['没有找到匹配的作品。', 'No matching works.'],
  reset: ['清除筛选', 'Clear filters'],
  credits: ['素材署名', 'Media credits'],
  contribute: ['推荐作品 ↗', 'Suggest a work ↗'],
  all: ['全部', 'All'],
  category: ['作品分类', 'Categories'],
  try: ['试玩 ↗', 'Play ↗'],
  watch: ['看演示', 'Watch demo'],
  details: ['详情', 'Details'],
  source: ['原始出处 ↗', 'Original source ↗'],
  media: ['画面出处 ↗', 'Preview source ↗'],
  output: ['查看作品 ↗', 'View work ↗'],
  guide: ['制作教程 ↗', 'Making-of guide ↗'],
  tools: ['制作信息', 'Production notes'],
  pending: ['画面待补 · 可查看原出处', 'Preview pending · original source available'],
  close: ['关闭详情', 'Close details'],
  playVideo: ['播放原演示 ↗', 'Open original video ↗'],
};

const state = new URLSearchParams(location.search);
let lang = state.get('lang') === 'zh' ? 0 : 1;
let category = Object.hasOwn(catalog.categories, state.get('category')) ? state.get('category') : '';
const t = key => copy[key][lang];
const title = work => work.title[lang];
const grid = $('grid');
const dialog = $('detail');
const works = catalog.works;
const chapterByCategory = new Map(Object.keys(catalog.categories)
  .map((key, index) => [key, ['I', 'II', 'III', 'IV', 'V'][index] || String(index + 1)]));
const positions = new Map(Object.keys(catalog.categories)
  .flatMap(key => works.filter(work => work.category === key))
  .map((work, index) => [work.id, String(index + 1).padStart(2, '0')]));

function node(tag, text, className) {
  const element = document.createElement(tag);
  if (text) element.textContent = text;
  if (className) element.className = className;
  return element;
}

function link(text, url) {
  const element = node('a', text);
  element.href = url;
  element.target = '_blank';
  element.rel = 'noopener noreferrer';
  return element;
}

function button(text, action, className) {
  const element = node('button', text, className);
  element.type = 'button';
  element.addEventListener('click', action);
  return element;
}

function image(work, lazy = true) {
  const img = node('img');
  img.alt = title(work);
  img.loading = lazy ? 'lazy' : 'eager';
  img.decoding = 'async';
  img.src = work.image;
  return img;
}

function openDetail(work) {
  const body = $('detail-body');
  body.replaceChildren();
  const media = node('div', '', 'detail-media');
  if (work.video) {
    const player = node('video');
    player.controls = true;
    player.playsInline = true;
    player.preload = 'none';
    if (work.image) player.poster = work.image;
    player.src = work.video;
    player.setAttribute('aria-label', title(work));
    media.append(player);
  } else if (work.image) {
    const img = image(work, false);
    img.addEventListener('error', () => img.remove());
    media.append(img);
  }
  body.append(media);
  const content = node('section', '', 'detail-content');
  const heading = node('h2', title(work));
  heading.id = 'detail-title';
  content.append(node('p', catalog.categories[work.category][lang], 'detail-category'), heading);
  if (work.summary[lang]) content.append(node('p', work.summary[lang]));
  if (!work.image && !work.video) content.append(node('p', t('pending')));
  const links = node('div', '', 'detail-links');
  if (work.play) links.append(link(t('try'), work.play));
  else if (work.output !== work.source && work.output !== work.video) links.append(link(t('output'), work.output));
  links.append(link(work.publisher + ' · ' + t('source'), work.source));
  if (work.guide) links.append(link(t('guide'), work.guide));
  if (work.video) links.append(link(t('playVideo'), work.video));
  if (work.image && work.imageSource !== work.source && work.imageSource !== work.video) links.append(link(t('media'), work.imageSource));
  content.append(links);
  if (work.variants.length) {
    const list = node('ul', '', 'variants');
    for (const variant of work.variants) {
      const item = node('li');
      if (variant.image) item.append(image(variant));
      const text = node('div');
      text.append(node('strong', title(variant)));
      const refs = node('p');
      refs.append(link(variant.publisher + ' ↗', variant.source));
      if (variant.play || variant.output !== variant.source) refs.append(' · ', link(t(variant.play ? 'try' : 'output'), variant.play || variant.output));
      if (variant.video && variant.video !== variant.output) refs.append(' · ', link(t('playVideo'), variant.video));
      text.append(refs);
      if (variant.tools) text.append(node('p', variant.tools));
      item.append(text);
      list.append(item);
    }
    content.append(node('h3', lang ? 'Works in this collection' : '专题里的作品'), list);
  } else if (work.tools || work.note[lang]) {
    const notes = node('details');
    notes.append(node('summary', t('tools')));
    if (work.tools) notes.append(node('p', work.tools));
    if (work.note[lang]) notes.append(node('p', work.note[lang]));
    content.append(notes);
  }
  body.append(content);
  dialog.scrollTop = 0;
  dialog.showModal();
}

function card(work) {
  const article = node('article', '', 'card');
  article.dataset.id = work.id;
  const cover = button('', () => openDetail(work), 'cover');
  cover.setAttribute('aria-label', title(work) + ' · ' + t('details'));
  cover.append(node('span', t('pending'), 'cover-fallback'));
  if (work.image) {
    const img = image(work);
    img.addEventListener('error', () => { cover.dataset.failed = 'true'; });
    cover.append(img);
  }
  if (work.variants.length) {
    cover.append(node('span', lang ? `${work.variants.length} works` : `${work.variants.length} 个作品`, 'cover-label'));
  }
  const caption = node('div', '', 'card-caption');
  const number = node('span', positions.get(work.id), 'card-number');
  number.setAttribute('aria-hidden', 'true');
  const h = node('h3');
  h.append(button(title(work), () => openDetail(work)));
  caption.append(number, h);
  const bottom = node('div', '', 'card-bottom');
  bottom.append(node('span', work.publisher), work.play ? link(t('try'), work.play) :
    button(t(work.video ? 'watch' : 'details'), () => openDetail(work)));
  article.append(cover, caption, bottom);
  return article;
}

function matches() {
  const tokens = $('search').value.normalize('NFKC').trim().toLowerCase().split(/\s+/).filter(Boolean);
  return works.filter(w => {
    if (category && w.category !== category) return false;
    if ($('playable').checked && !w.play) return false;
    if (!tokens.length) return true;
    const text = [w.title, w.publisher, w.summary, w.tags, catalog.categories[w.category],
      ...w.variants.map(v => [v.title, v.publisher])].flat(Infinity).join(' ').normalize('NFKC').toLowerCase();
    return tokens.every(term => text.includes(term));
  });
}

function render() {
  const filtered = matches();
  const sections = [];
  for (const [key, names] of Object.entries(catalog.categories)) {
    const entries = filtered.filter(w => w.category === key);
    if (!entries.length) continue;
    const heading = node('h3', '', 'grid-heading');
    const chapter = node('span', chapterByCategory.get(key), 'chapter-number');
    chapter.setAttribute('aria-hidden', 'true');
    heading.append(chapter, node('span', names[lang], 'chapter-title'),
      node('span', lang ? `${entries.length} entries` : `${entries.length} 项`, 'section-count'));
    sections.push(heading);
    sections.push(...entries.map(card));
  }
  grid.replaceChildren(...sections);
  $('count').textContent = filtered.length === works.length
    ? (lang ? `${works.length} works and collections` : `${works.length} 个作品与专题`)
    : (lang ? `${filtered.length} of ${works.length}` : `找到 ${filtered.length} / ${works.length} 个`);
  $('empty').hidden = filtered.length !== 0;
}

function renderCategories() {
  $('categories').setAttribute('aria-label', t('category'));
  $('categories').replaceChildren(...[['', t('all')], ...Object.entries(catalog.categories).map(([key, names]) => [key, names[lang]])]
    .map(([key, label]) => {
      const control = button(label, () => {
        const gallery = $('gallery');
        const wasScrolled = gallery.getBoundingClientRect().top < 0;
        category = key;
        for (const btn of $('categories').children) btn.setAttribute('aria-pressed', String(btn === control));
        render();
        if (wasScrolled) gallery.scrollIntoView({block: 'start'});
      });
      control.setAttribute('aria-pressed', String(category === key));
      if (key) {
        const marker = node('span', chapterByCategory.get(key), 'tab-number');
        marker.setAttribute('aria-hidden', 'true');
        control.prepend(marker);
      }
      return control;
    }));
}

function localize() {
  document.documentElement.lang = lang ? 'en' : 'zh-CN';
  document.title = lang ? 'Awesome AI Fun · Gallery' : 'Awesome AI Fun · 作品画廊';
  for (const element of document.querySelectorAll('[data-copy]')) element.textContent = t(element.dataset.copy);
  $('search').placeholder = t('searchHint');
  $('language').textContent = lang ? '简体中文' : 'English';
  $('language').lang = lang ? 'zh-CN' : 'en';
  $('close').setAttribute('aria-label', t('close'));
  $('credits').href = 'https://github.com/Java4ye/awesome-ai-fun/blob/main/docs/' + (lang ? 'en/' : '') + 'THIRD_PARTY_MEDIA.md';
  $('suggest').href = 'https://github.com/Java4ye/awesome-ai-fun/issues/new?template=new-case' + (lang ? '-en' : '') + '.md';
  $('prompt-label').textContent = lang ? `Hands-on prompts · ${catalog.prompts.length}` : `动手题库 · ${catalog.prompts.length} 道题`;
  $('prompts').replaceChildren(...catalog.prompts.map(p => {
    const item = node('li');
    item.append(link(p.title[lang], p.source));
    return item;
  }));
  renderCategories();
  render();
}

$('search').value = state.get('q') || '';
$('playable').checked = state.get('playable') === '1';
$('search').addEventListener('input', render);
$('playable').addEventListener('change', render);
$('language').addEventListener('click', () => {
  lang = 1 - lang;
  const url = new URL(location.href);
  if (lang) url.searchParams.delete('lang');
  else url.searchParams.set('lang', 'zh');
  try { history.replaceState(null, '', url); } catch { /* Language switching still works when URL updates are restricted. */ }
  localize();
});
$('reset').addEventListener('click', () => {
  $('search').value = '';
  $('playable').checked = false;
  category = '';
  renderCategories();
  render();
  $('search').focus();
});
$('close').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => $('detail-body').replaceChildren());
localize();
