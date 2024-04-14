/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html',
  '**/templates/**/*.html'],
  darkMode: "class",
  theme: {
    extend: {

      colors: {

        "brown": {
          100: "#ECE0D1",
          300: "#DBC1AC",
          600: "#967259",
          900: "#634832"
        }
      },

      boxShadow: {
        "normal": "0px 1px 10px rgba(0, 0, 0, 0.05)",
      },

      borderRadius: {
        "4xl": "2rem",
      },

      fontFamily: {
        "Dana": "Dana",
        "DanaMedium": "Dana Medium",
        "DanaDemiBold": "Dana DemiBold",
        "Morabba": "Morabba Light",
        "MorabbaMedium": "Morabba Medium",
        "MorabbaBold": "Morabba Bold"
      },

      letterSpacing: {
        "tightest": "-0.65"
      },

      spacing: {
        "4.5": "1.125rem",
        "30": "7.5rem",
        "25": "6.25rem",
        "50": "12.5rem",
      },

      container: {
          center: true,
          padding: {
            DEFAULT: "1rem",
            lg: "0.625rem", 
          }
      }
    },
    screens: {
      'xs': '480px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
    },

    backgroundImage: {
      "home-mobile": "url(../images/headerBgMobile.webp)",
      "home-desktop": "url(../images/headerBgDesktop.webp)",
     }

  },
  plugins: [
    function ({addVariant}) {
      addVariant('child', '& > *');
      addVariant('child-hove', '& > *:hover');
    }
  ],
}

