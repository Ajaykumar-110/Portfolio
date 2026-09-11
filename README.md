# Ajaykumar M - Full Stack Developer Portfolio

A premium, modern portfolio website for Ajaykumar M, a Full Stack Developer. Built with React, Tailwind CSS, Framer Motion, and Lucide Icons.

- **Live Production URL**: [https://ajaykumar-me.vercel.app](https://ajaykumar-me.vercel.app)
- **Alternative Production URL**: [https://ajaykumar-fullstack.vercel.app](https://ajaykumar-fullstack.vercel.app)
- **Custom Domain Configured**: `ajaykumar.me`

## 🎨 Design Features

- **Premium Dark UI**: Inspired by Linear, Vercel, and modern SaaS products
- **Smooth Animations**: Scroll-triggered reveals, fade-ins, and micro-interactions
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Accessibility First**: Semantic HTML, keyboard navigation, and ARIA attributes
- **Performance Optimized**: Fast loading, optimized animations, minimal dependencies
- **Professional Components**: Reusable, well-organized React components

## 📊 Color Scheme

```
Background:        #0B0F19 (Deep Navy)
Secondary BG:      #111827 (Charcoal)
Cards:             #151B2B (Card Background)
Primary Text:      #F8FAFC (Clean White)
Secondary Text:    #94A3B8 (Muted Slate)
Accent Blue:       #0EA5E9 (Electric Blue)
Accent Violet:     #A855F7 (Violet)
```

## 🚀 Quick Start

### Prerequisites
- Node.js 14+ and npm/yarn

### Installation

```bash
# Navigate to project directory
cd portfolio

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The portfolio will open at `http://localhost:3000`

## 📁 Project Structure

```
src/
├── components/
│   ├── Navbar.jsx          # Sticky navigation with blur effect
│   ├── Hero.jsx            # Hero section with code editor visual
│   ├── About.jsx           # About section with profile card
│   ├── Skills.jsx          # Technical skills organized by category
│   ├── Experience.jsx      # Experience timeline
│   ├── Projects.jsx        # Featured projects with modal details
│   ├── Education.jsx       # Education information
│   ├── GitHubSection.jsx   # GitHub profile section
│   ├── Contact.jsx         # Contact form and information
│   └── Footer.jsx          # Footer with links
├── data/
│   └── portfolio.js        # All portfolio content (single source of truth)
├── App.jsx                 # Main app component
├── main.jsx                # React entry point
└── index.css               # Global styles

Configuration Files:
├── vite.config.js          # Vite configuration
├── tailwind.config.js      # Tailwind CSS custom theme
├── postcss.config.js       # PostCSS configuration
├── package.json            # Project dependencies
└── index.html              # HTML entry point
```

## 🎯 Page Structure

1. **Navbar** - Sticky navigation with smooth blur effect
2. **Hero** - Impressive headline with code editor visual
3. **About** - Professional introduction with profile highlights
4. **Skills** - Technical arsenal organized in categories
5. **Experience** - Timeline of work experience
6. **Projects** - Featured full-stack projects with detailed modals
7. **Education** - Academic credentials
8. **GitHub** - Developer presence and public building
9. **Contact** - Contact form and direct messaging
10. **Footer** - Social links and copyright

## 🛠️ Technologies Used

- **React 18** - UI framework
- **Tailwind CSS 3** - Utility-first CSS
- **Framer Motion** - Animation library
- **Lucide React** - Icon library
- **Vite** - Build tool and dev server
- **PostCSS** - CSS processing

## 📝 Customization Guide

### Updating Portfolio Content

All content is stored in `src/data/portfolio.js`. Edit this file to update:
- Personal information (name, email, phone, social links)
- Hero section text and CTAs
- About section content
- Skills and categories
- Experience entries
- Projects and project details
- Education information
- Contact information

**Important**: Only update content in `portfolio.js`. Do not hardcode content in components.

### Changing Colors

Update colors in `tailwind.config.js` under `extend.colors`:

```javascript
colors: {
  'dark-bg': '#0B0F19',
  'dark-secondary': '#111827',
  'dark-card': '#151B2B',
  'text-primary': '#F8FAFC',
  'text-secondary': '#94A3B8',
  'accent-blue': '#0EA5E9',
  'accent-violet': '#A855F7',
}
```

### Modifying Typography

Typography scale is defined in `tailwind.config.js`:

```javascript
fontSize: {
  'display-xl': ['80px', { lineHeight: '1.1', fontWeight: '700' }],
  'display-lg': ['64px', { lineHeight: '1.1', fontWeight: '700' }],
  'section-lg': ['48px', { lineHeight: '1.2', fontWeight: '700' }],
  // ... more sizes
}
```

### Adding Animations

Animations are configured in `tailwind.config.js` and used with Framer Motion:

```javascript
animation: {
  'fade-in': 'fadeIn 0.6s ease-out',
  'slide-up': 'slideUp 0.6s ease-out',
}
```

Use with `motion` components:
```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6 }}
>
  Content
</motion.div>
```

## 📦 Deployment

### Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

Vercel automatically detects Vite and builds the project.

### Deploy to Netlify

```bash
# Build the project
npm run build

# Install Netlify CLI
npm i -g netlify-cli

# Deploy
netlify deploy --prod --dir=dist
```

### Deploy to Other Platforms

1. Build the project: `npm run build`
2. Upload the `dist` folder to your hosting provider
3. Set build command to: `npm run build`
4. Set publish directory to: `dist`

### GitHub Pages

```bash
# Update vite.config.js to set base:
# base: '/repository-name/'

npm run build
# Then push dist folder to gh-pages branch
```

## 🌐 Domain Setup

After deployment, you can:

1. Configure custom domain through your hosting provider
2. Update social links in `portfolio.js` to point to your domain
3. Set up email forwarding for contact form responses
4. Add analytics (Google Analytics, Posthog, etc.)

## ✨ Key Features

✅ **Premium Dark UI** - Inspired by Linear, Vercel, and modern SaaS  
✅ **Smooth Animations** - Scroll reveals, hover effects, micro-interactions  
✅ **Fully Responsive** - Works perfectly on all device sizes  
✅ **Accessibility** - Semantic HTML, keyboard navigation, ARIA attributes  
✅ **Performance** - Optimized for fast loading and Lighthouse scores  
✅ **SEO Ready** - Meta tags, semantic markup, structured data  
✅ **Developer Friendly** - Clean code, organized components, reusable patterns  
✅ **Easy to Customize** - Change content, colors, and animations easily  

## 📱 Responsive Breakpoints

- **Mobile**: < 768px (single column, hamburger menu)
- **Tablet**: 768px - 1024px (adaptive layout)
- **Desktop**: > 1024px (full features, two-column layouts)

## ♿ Accessibility Features

- Semantic HTML5 structure
- Proper heading hierarchy (h1 → h6)
- ARIA labels on interactive elements
- Keyboard navigation support
- Focus indicators on interactive elements
- Color contrast compliant (WCAG AA)
- Form validation and error messages

## 🎯 Performance Optimization

- Lazy-loaded images and sections
- Minimal JavaScript dependencies
- Optimized CSS with Tailwind
- Smooth animations (GPU-accelerated)
- Responsive images
- Clean React architecture

## 📊 Lighthouse Targets

- **Performance**: 90+
- **Accessibility**: 95+
- **Best Practices**: 95+
- **SEO**: 100

## 🔧 Troubleshooting

### Animations not working
- Check if Framer Motion is installed: `npm install framer-motion`
- Ensure reduced motion preferences are respected in browser settings

### Tailwind classes not applied
- Clear cache: `rm -rf node_modules/.cache`
- Rebuild: `npm run build`

### Font not loading
- Check internet connection
- Verify Google Fonts are accessible in your region

### Contact form not working
- This is a demo form. To enable email functionality, set up a backend service
- Use services like Formspree, EmailJS, or your own backend

## 📄 License

This portfolio is created for Ajaykumar M. All rights reserved.

## 🙋 Support

For issues or customizations, refer to:
- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [Framer Motion](https://www.framer.com/motion/)
- [Lucide Icons](https://lucide.dev)
- [Vite Documentation](https://vitejs.dev)

---

**Built with ❤️ using React, Tailwind CSS, and Framer Motion**
