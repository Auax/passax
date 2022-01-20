module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                "c-gray": "#2f314b",
                "c-dark-gray" : "#191919",
                "c-dark-blue": "#0f172a",
                "c-light-purple": "#8173ff",
            }
        },
    },
    plugins: [
        require('daisyui'),
    ],
}