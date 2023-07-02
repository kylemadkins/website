/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        blue: "#315fe7",
      },
      fontFamily: {
        sans: ["'Karla'", "sans-serif"],
        mono: ["'IntelOne Mono'", "monospace"],
        display: ["'Press Start 2P'", "cursive"]
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
