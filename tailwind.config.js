/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'dark-bg': '#0B0F19',
        'dark-secondary': '#111827',
        'dark-card': '#151B2B',
        'text-primary': '#F8FAFC',
        'text-secondary': '#94A3B8',
        'accent-blue': '#0EA5E9',
        'accent-violet': '#A855F7',
      },
      fontFamily: {
        'display': ['Geist', 'system-ui', 'sans-serif'],
        'body': ['Inter', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        'display-xl': ['80px', { lineHeight: '1.1', fontWeight: '700' }],
        'display-lg': ['64px', { lineHeight: '1.1', fontWeight: '700' }],
        'section-lg': ['48px', { lineHeight: '1.2', fontWeight: '700' }],
        'section': ['40px', { lineHeight: '1.2', fontWeight: '700' }],
        'card-lg': ['24px', { lineHeight: '1.3', fontWeight: '600' }],
        'card': ['20px', { lineHeight: '1.3', fontWeight: '600' }],
        'body-lg': ['18px', { lineHeight: '1.6' }],
        'body-base': ['16px', { lineHeight: '1.6' }],
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        'card': '0 4px 6px rgba(0, 0, 0, 0.07), 0 10px 13px rgba(0, 0, 0, 0.1)',
        'card-hover': '0 20px 25px rgba(0, 0, 0, 0.1), 0 25px 50px rgba(0, 0, 0, 0.15)',
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
