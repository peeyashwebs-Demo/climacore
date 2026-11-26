# Climacore website (rebuild)
Static site (HTML/CSS/JS). Open `index.html` to preview, or deploy the folder (Vercel config in `vercel.json`).

**Content source:** everything factual comes from climacoreair.com (contact details, license no., 16 counties, services, FAQs, prices quoted there, reviews, blog posts, financing and membership details). Nothing is invented.
- Contact form = Climacore's own Jotform (embedded on `contact.html`). Online booking = their Housecall Pro link. Financing = CoolNow™. Membership = Cool Club. Terms/Privacy link to their site.
- Edit copy or company details in `tools/build_site.py`, then run `python3 tools/build_site.py` to regenerate all pages. Phone number also lives in `js/main.js` (`SITE`).
- Logo and blog/van photos load from climacoreair.com; if unreachable they fall back to a text wordmark / local illustrations. For reliability, save the logo and photos into `assets/` and point the build script at them.
- Illustrations in `assets/images/` are generic vector art (`tools/make_images.py`); replace with real project photos when available.
