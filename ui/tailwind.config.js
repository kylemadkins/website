/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        link: "#544ddd",
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
