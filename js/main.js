/* Climacore site: shared behavior. Company details below are taken from climacoreair.com. */
const SITE = { name: "Climacore", phone: "3214624141", license: "CAC 1823663", bookUrl: "https://book.housecallpro.com/book/Climacore/2564e5d770c24f239c4c5b86f63f09e0?v2=true" };
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
$$("[data-call]").forEach(a => { a.href = "tel:+1" + SITE.phone; });
$$("[data-year]").forEach(e => e.textContent = new Date().getFullYear());

/* Mobile menu */
const mb = $(".menu-btn"), menu = $("#menu");
mb.addEventListener("click", () => { const o = menu.classList.toggle("open"); mb.setAttribute("aria-expanded", o); });
$$("#menu a").forEach(a => a.addEventListener("click", () => { menu.classList.remove("open"); mb.setAttribute("aria-expanded", false); }));
addEventListener("keydown", e => { if (e.key === "Escape") { menu.classList.remove("open"); mb.setAttribute("aria-expanded", false); } });

/* Images from climacoreair.com fall back to local art (or a text wordmark for the logo) if they can't load */
const fix = i => {
  if (i.dataset.fb && !i.dataset.done) { i.dataset.done = 1; i.src = i.dataset.fb; }
  else if (i.classList.contains("logo-img")) i.replaceWith(Object.assign(document.createElement("span"), { className: "lw", textContent: "✻ Climacore" }));
};
document.addEventListener("error", e => { if (e.target.tagName === "IMG") fix(e.target); }, true);
addEventListener("load", () => $$("img[data-fb],img.logo-img").forEach(i => { if (i.complete && !i.naturalWidth) fix(i); }));

/* Reveal once on scroll (skipped for reduced motion) */
if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion:reduce)").matches) {
  const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }), { threshold: .12 });
  $$(".reveal").forEach(el => io.observe(el));
} else $$(".reveal").forEach(el => el.classList.add("in"));
