module.exports = {
    purge: ['./public/index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    theme: {
        fontFamily: {
            sans: ['Poppins', 'ui-sans-serif', 'system-ui'],
            header: ['Poppins', 'ui-sans-serif', 'system-ui'],
        },
        extend: {
            colors: {
                surface: {
                    900: '#05060a',
                    800: '#0b1220',
                    700: '#0f1724',
                    DEFAULT: '#0b1220'
                },
                primary: {
                    DEFAULT: '#7C3AED',
                    600: '#6d28d9'
                },
                accent: {
                    DEFAULT: '#06B6D4',
                    400: '#2dd4bf'
                },
                card: '#0f1724'
            },
            boxShadow: {
                'lg-soft': '0 10px 25px rgba(2,6,23,0.6)'
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
