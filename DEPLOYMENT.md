# Portfolio Deployment & Launch Guide

This guide walks through deploying your premium portfolio website for recruiters.

## Pre-Deployment Checklist

- [ ] All content verified in `src/data/portfolio.js`
- [ ] Email address is correct: `majaykumar0520@gmail.com`
- [ ] GitHub link is correct: `github.com/Ajaykumar-110`
- [ ] LinkedIn profile link is correct
- [ ] Project links (GitHub repos and live demos) are accurate
- [ ] No placeholder text remains
- [ ] All sections are complete and reviewed
- [ ] Contact form disclaimer is present

## Step 1: Local Testing

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Test all sections:
# - Navbar responsiveness and navigation
# - Hero section animations
# - All links (social, GitHub, LinkedIn)
# - Contact form validation
# - Mobile responsiveness
# - Animations and transitions
```

## Step 2: Production Build

```bash
# Build for production
npm run build

# Test production build
npm run preview

# Check if everything works correctly
```

## Step 3: Choose Deployment Platform

### Option A: Vercel (Recommended for React)

**Pros**: Optimal for React/Vite, auto-deploy from Git, free tier generous, CDN included

```bash
# 1. Create Vercel account at vercel.com
# 2. Install Vercel CLI
npm i -g vercel

# 3. Deploy
vercel

# Follow prompts (select framework: Vite, project name, etc.)
# Your portfolio is now live!
```

**Custom Domain on Vercel**:
```bash
vercel env add NEXT_PUBLIC_DOMAIN your-domain.com
# Then configure domain in Vercel dashboard
```

### Option B: Netlify

**Pros**: User-friendly, generous free tier, good documentation

```bash
# 1. Create Netlify account at netlify.com
# 2. Connect GitHub repository
# 3. Netlify auto-deploys on every push
# 4. Alternatively, manual deployment:

npm run build
npm i -g netlify-cli
netlify deploy --prod --dir=dist
```

**Configure in netlify.toml**:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[context.production]
  command = "npm run build"
```

### Option C: GitHub Pages

```bash
# Update vite.config.js:
# base: '/ajaykumar-portfolio/' (if using username.github.io/repo-name)
# or base: '/' (if using username.github.io)

npm run build

# Push dist folder to gh-pages branch
# Enable GitHub Pages in repository settings
```

### Option D: Self-Hosted (VPS)

```bash
# 1. SSH into your server
ssh user@your-server.com

# 2. Clone repository and build
git clone https://github.com/yourusername/portfolio.git
cd portfolio
npm install
npm run build

# 3. Serve with Nginx or Apache
# Copy dist folder to /var/www/html
# Configure reverse proxy if needed
```

## Step 4: Post-Deployment

### 1. Verify Deployment

- [ ] Visit deployed URL
- [ ] Check all pages load correctly
- [ ] Test responsive design (mobile, tablet, desktop)
- [ ] Verify all external links work
- [ ] Check animations and transitions
- [ ] Test contact form (demo form won't send, but validation should work)

### 2. Add Analytics (Optional)

```javascript
// Add to index.html before </head>
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### 3. Set Up Email Forwarding

For contact form to work, use one of these services:

**Option 1: Formspree** (Recommended)
```javascript
// Update Contact.jsx handleSubmit:
const response = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
  method: 'POST',
  body: JSON.stringify(formData),
});
```

**Option 2: EmailJS**
```javascript
import emailjs from '@emailjs/browser';

emailjs.init('YOUR_PUBLIC_KEY');

const sendEmail = async () => {
  await emailjs.send('SERVICE_ID', 'TEMPLATE_ID', formData);
};
```

**Option 3: Backend API**
- Create your own Express backend
- Handle form submissions securely
- Send emails via nodemailer or similar

### 4. Configure Custom Domain

1. Purchase domain (GoDaddy, Namecheap, Domain.com, etc.)
2. Update DNS records to point to your hosting provider
3. Set up SSL/HTTPS certificate (usually automatic)
4. Update social links in `portfolio.js` to use new domain

**For Vercel**:
```bash
vercel domains add your-domain.com
# Then configure DNS records
```

**For Netlify**:
- Add domain in Netlify dashboard
- Update DNS records
- Certificate auto-provisioned

## Step 5: Ongoing Maintenance

### Update Portfolio Content

1. Edit `src/data/portfolio.js` with new information
2. Commit changes to Git
3. Deployment platform auto-builds and deploys (if using Git integration)

### Monitor Performance

- Use Lighthouse to check performance scores
- Check analytics for traffic and engagement
- Monitor error logs
- Test contact form responses

### Security Updates

```bash
# Check for vulnerabilities
npm audit

# Update dependencies
npm update

# Keep Node.js updated
node --version
```

## Troubleshooting Deployment

### Site shows 404

- Verify build completed successfully
- Check publish directory is `dist` (not `build` or other)
- Ensure base URL is correct in vite.config.js

### Styles not loading

- Clear browser cache (Ctrl+Shift+Delete)
- Verify Tailwind CSS was built correctly
- Check CSS files in dist folder

### Animations not working

- Ensure Framer Motion is in dist output
- Check browser console for errors
- Verify reduced motion preferences

### Slow loading

- Optimize images
- Enable gzip compression on server
- Use CDN for static assets
- Minify CSS and JavaScript

### Contact form not working

- Verify form is demo-only (won't actually send without backend)
- Implement one of the email solutions mentioned above
- Check browser console for errors

## Performance Optimization Checklist

- [ ] Images are optimized and compressed
- [ ] CSS is minified
- [ ] JavaScript is minified and tree-shaken
- [ ] Unused dependencies removed
- [ ] Service worker configured (optional)
- [ ] Cache headers configured on server
- [ ] CDN enabled for static assets
- [ ] Critical CSS inlined (optional)
- [ ] Lazy loading enabled for images
- [ ] Lighthouse score > 90 for all metrics

## SEO Optimization

- [ ] Meta tags updated in index.html
- [ ] Open Graph tags configured
- [ ] Twitter Card tags added
- [ ] Sitemap.xml generated (if using backend)
- [ ] robots.txt configured
- [ ] Schema.org structured data added
- [ ] All internal links working
- [ ] Mobile-friendly design verified

## Share Your Portfolio

Once live:

1. **LinkedIn**
   - Update profile with portfolio link
   - Add portfolio URL in About section
   - Create post announcing your new portfolio

2. **GitHub**
   - Link portfolio in profile
   - Star relevant MERN projects
   - Make repositories public with good READMEs

3. **Email**
   - Add to email signature
   - Send to recruiters and connections
   - Include in applications

4. **Resume**
   - Add portfolio link to resume
   - Update LinkedIn URL

5. **Social Media**
   - Share on Twitter/X
   - Post on relevant dev communities
   - Add to Discord/Slack profiles

## Monitoring & Analytics

```bash
# Set up email alerts for:
# - Site downtime
# - Performance degradation
# - High error rates
# - Traffic spikes
```

Services to consider:
- **Vercel Analytics** - Built-in for Vercel
- **Google Analytics** - Free comprehensive analytics
- **Posthog** - Privacy-first analytics
- **Sentry** - Error tracking

## Final Checklist

- [ ] Domain configured and working
- [ ] SSL/HTTPS certificate active
- [ ] All content is accurate and up-to-date
- [ ] Contact form properly configured
- [ ] Analytics setup (optional)
- [ ] Email forwarding working
- [ ] Performance optimized
- [ ] SEO optimized
- [ ] Mobile responsive verified
- [ ] Accessibility verified
- [ ] Portfolio shared with target audience
- [ ] Linked from GitHub profile
- [ ] Linked from LinkedIn profile
- [ ] Added to email signature and resume

## Success! 🎉

Your portfolio is now live and ready to impress recruiters! 

**Next Steps**:
1. Keep sharing your portfolio
2. Update projects as you build new ones
3. Add testimonials/recommendations
4. Monitor performance metrics
5. Stay in touch with connections through your portfolio

Good luck with your placement journey! 🚀
