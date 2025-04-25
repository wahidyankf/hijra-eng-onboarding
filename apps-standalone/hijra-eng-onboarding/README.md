# Hijra Onboarding

This is the codebase for hijra onboarding documentation site. It uses [Hugo](https://gohugo.io) with the [Hextra](https://github.com/imfing/hextra) theme for a beautiful documentation experience.

## Features

- Built with Hugo for blazing-fast performance
- Clean, modern UI with custom styling (including hidden scrollbars)
- Multi-language content support
- Responsive design for all devices
- Search functionality
- Dark/light mode support

## How to Run

```shell
# Development server with hot reload
npm run dev

# Build for production
npm run build
```

## Content

Place your content in the `content` directory. The site structure follows Hugo conventions:

```
content/
├── _index.md         # Home page
├── docs/             # Documentation pages
│   └── ...
├── blog/             # Blog posts
│   └── ...
└── about/            # About pages
    └── ...
```

## Custom Styling

This site includes custom styling for a cleaner UI experience, including hidden scrollbars. These custom styles are added directly to the layout's head.html template.

## Deployment

The site is built using the `npm run build` command and can be deployed to any static hosting provider.

## License

MIT License
