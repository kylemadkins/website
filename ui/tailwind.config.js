/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        blue: "#315fe7",
      },
      fontFamily: {
        sans: ["Karla", "sans-serif"],
        serif: ["Young Serif", "serif"],
        mono: ["Space Mono", "monospace"],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
