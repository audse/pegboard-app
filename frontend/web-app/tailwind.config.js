module.exports = {
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {
            'main': 'var(--primary)',
            'second': 'var(--secondary)',
            'text': 'var(--text)',
            'emphasis': 'var(--emphasis)',
            'alert': 'var(--alert)',

            'scale-text-100': 'var(--scale-text-100)',
            'scale-text-300': 'var(--scale-text-300)',
            'scale-text-500': 'var(--scale-text-500)',
            'scale-text-700': 'var(--scale-text-700)',
            'scale-text-900': 'var(--scale-text-900)',

            'scale-secondary-100': 'var(--scale-secondary-100)',
            'scale-secondary-300': 'var(--scale-secondary-300)',
            'scale-secondary-500': 'var(--scale-secondary-500)',
            'scale-secondary-700': 'var(--scale-secondary-700)',
            'scale-secondary-900': 'var(--scale-secondary-900)',
        },
        extend: {
            backdropInvert: {
                5: '.05',
                10: '.10',
                25: '.25',
                75: '.75',
                90: '.9',
                95: '.95'
            },
            strokeWidth: {
                '05': '0.5',
            }
        },
    },
    variants: {
        extend: {
            backgroundColor: ['checked'],
            borderColor: ['checked'],
        },
    },

    plugins: [
        require('daisyui'),
    ],

    daisyui: {
      styled: true,
      themes: [
        { 'colors': {
            'primary': 'var(--primary)',
            'primary-focus': 'var(--primary)',
            'primary-content': 'var(--text)',

            'secondary': 'var(--secondary)',
            'secondary-focus': 'var(--secondary)',
            'secondary-content': 'var(--text)',

            'info': 'var(--info)',
            'warning': 'var(--warning)',
            'error': 'var(--error)',
        }},
      ],
      base: true,
      utils: true,
      logs: true,
      rtl: false,
    },
}
