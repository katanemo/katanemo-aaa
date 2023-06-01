/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,jsx,ts,tsx}',
    './src/components/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
        colors: {
            'primary': '#1a202c',
            'secondary': '#2d3748',
        }
    },
  },
  plugins: [],
}

