module.exports = {
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {
            'main': 'var(--main)',
            'second': 'var(--second)',
            'text': 'var(--text)',

            'emphasis': 'var(--emphasis)',
            'emphasis-opacity-50': 'var(--emphasis-opacity-50)',
            'emphasis-opacity-100': 'var(--emphasis-opacity-100)',
            'emphasis-opacity-300': 'var(--emphasis-opacity-300)',
            'emphasis-opacity-500': 'var(--emphasis-opacity-500)',
            'emphasis-opacity-700': 'var(--emphasis-opacity-700)',
            'emphasis-opacity-900': 'var(--emphasis-opacity-900)',

            'alert': 'var(--alert)',
            'danger': 'var(--danger)',

            'scale-text-50': 'var(--scale-text-50)',
            'scale-text-100': 'var(--scale-text-100)',
            'scale-text-200': 'var(--scale-text-200)',
            'scale-text-300': 'var(--scale-text-300)',
            'scale-text-400': 'var(--scale-text-400)',
            'scale-text-500': 'var(--scale-text-500)',
            'scale-text-600': 'var(--scale-text-600)',
            'scale-text-700': 'var(--scale-text-700)',
            'scale-text-800': 'var(--scale-text-800)',
            'scale-text-900': 'var(--scale-text-900)',

            'scale-secondary-50': 'var(--scale-secondary-50)',
            'scale-secondary-100': 'var(--scale-secondary-100)',
            'scale-secondary-200': 'var(--scale-secondary-200)',
            'scale-secondary-300': 'var(--scale-secondary-300)',
            'scale-secondary-400': 'var(--scale-secondary-400)',
            'scale-secondary-500': 'var(--scale-secondary-500)',
            'scale-secondary-600': 'var(--scale-secondary-600)',
            'scale-secondary-700': 'var(--scale-secondary-700)',
            'scale-secondary-800': 'var(--scale-secondary-800)',
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
      ],
      base: true,
      utils: true,
      logs: true,
      rtl: false,
    },
}
