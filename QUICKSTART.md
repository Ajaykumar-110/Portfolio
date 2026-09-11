# 🚀 Quick Start Guide

Get your portfolio running in 3 minutes!

## Prerequisites

Make sure you have **Node.js 14+** installed:
```bash
node --version  # Should be 14 or higher
npm --version   # Should be 6 or higher
```

If not installed, download from [nodejs.org](https://nodejs.org)

## Step 1: Install Dependencies (30 seconds)

```bash
cd portfolio
npm install
```

This installs React, Tailwind CSS, Framer Motion, and other dependencies.

## Step 2: Start Development Server (10 seconds)

```bash
npm run dev
```

Your browser will automatically open at `http://localhost:3000`

**You now have a fully functional portfolio!** 🎉

## Step 3: View Your Portfolio

Explore the site:
- Click through all sections
- Test mobile responsiveness (resize browser)
- Click all buttons and links
- Try the contact form
- Check animations on scroll

## Making Changes

All content is in one file: `src/data/portfolio.js`

Want to change something?

```javascript
// Example: Change email
personal: {
  email: 'your-new-email@example.com'
}

// Example: Update a skill
skills: {
  categories: [{
    name: 'Frontend',
    items: [
      { name: 'React.js', icon: 'react' },
      // Add/remove skills here
    ]
  }]
}
```

Save the file → Your browser automatically updates! (Hot reload enabled)

## Building for Deployment

When ready to share:

```bash
npm run build
```

This creates a `dist` folder with your production site.

## Deploy in 2 Minutes

### Option A: Vercel (Recommended)

```bash
npm install -g vercel
vercel
```

Answer the prompts and your site is **live!** 🎉

### Option B: Netlify

```bash
npm install -g netlify-cli
npm run build
netlify deploy --prod --dir=dist
```

### Option C: GitHub Pages

```bash
npm run build
# Then push dist folder and enable GitHub Pages in settings
```

See `DEPLOYMENT.md` for detailed instructions.

## Common Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build locally
npm run preview

# Check for code issues
npm run lint
```

## Customization Tips

### Change Colors

Edit `tailwind.config.js`:
```javascript
extend: {
  colors: {
    'accent-blue': '#0EA5E9',  // Change primary color
    'dark-bg': '#0B0F19',      // Change background
  },
}
```

### Change Fonts

Edit `tailwind.config.js`:
```javascript
fontFamily: {
  'display': ['Geist', 'system-ui', 'sans-serif'],
  'body': ['Inter', 'system-ui', 'sans-serif'],
}
```

### Add Animation

Edit component:
```jsx
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.6 }}
>
  Your content
</motion.div>
```

## Project Structure at a Glance

```
portfolio/
├── src/
│   ├── components/          # All page sections
│   ├── data/portfolio.js    # All your content ← EDIT THIS
│   └── App.jsx              # Main app
├── index.html               # HTML page
└── tailwind.config.js       # Colors & styling ← CUSTOMIZE HERE
```

## Troubleshooting

**"Module not found" error?**
```bash
rm -rf node_modules
npm install
```

**Port 3000 already in use?**
```bash
npm run dev -- --port 3001
```

**Styles not loading?**
- Clear browser cache (Ctrl+Shift+Delete)
- Restart dev server

**Changes not showing?**
- Save file and wait 1-2 seconds
- Refresh browser (F5)

## Next Steps

1. ✅ Run locally (`npm run dev`)
2. ✅ Explore the portfolio
3. ✅ Update your content in `src/data/portfolio.js`
4. ✅ Customize colors in `tailwind.config.js` (optional)
5. ✅ Build for production (`npm run build`)
6. ✅ Deploy to Vercel/Netlify/GitHub Pages
7. ✅ Share with recruiters!

## Need Help?

- **How do I deploy?** → Read `DEPLOYMENT.md`
- **How do I customize?** → Read `README.md`
- **What's included?** → Read `IMPLEMENTATION_SUMMARY.md`
- **React questions?** → [react.dev](https://react.dev)
- **Tailwind questions?** → [tailwindcss.com](https://tailwindcss.com)

## Performance Tip

For the best performance:
1. Keep animations subtle
2. Compress images if you add any
3. Minimize external dependencies
4. Deploy to Vercel (optimized for React)

## Share Your Portfolio

Once deployed:

1. **LinkedIn** - Add URL to profile
2. **GitHub** - Add link to README
3. **Resume** - Include portfolio link
4. **Email** - Add to signature
5. **Messages** - Share with recruiters

## Last Step: Ship It! 🚀

```bash
npm run build
vercel  # or your chosen platform
```

Your premium portfolio is now live! Congratulations! 🎉

---

**Questions?** Check the README.md or DEPLOYMENT.md files.

**Ready?** Run `npm run dev` and see your portfolio come to life!
