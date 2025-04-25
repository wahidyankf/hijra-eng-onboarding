# OSS Monorepo

## Overview

This monorepo is a comprehensive development workspace that includes multiple applications, libraries, and tools. It provides a flexible and scalable approach to managing different projects and standalone applications.

## Project Structure

```
oss/
├── apps/
│   ├── next-hello/   # Main Next.js web application integrated into the monorepo
│   └── web-e2e/      # End-to-end tests for the web application
├── apps-standalone/  # Apps that are hard/not yet integrated to the monorepo
│   └── hijra-eng-onboarding/  # Hugo-powered documentation site
├── libs/             # Shared libraries and components
│   └── ...           # Reusable code and shared utilities
├── scripts/          # Utility scripts for project management
└── tools/            # Development and build tools
```

### Folder Descriptions

#### Apps

- `next-hello`: The primary web application integrated into the monorepo
- `web-e2e`: End-to-end testing suite for the web application

#### Apps-Standalone

The `apps-standalone` folder is used for applications that are:

- Difficult to integrate into the monorepo
- Experimental projects
- Not yet ready for full monorepo integration
- Maintained separately from the main monorepo workflow

Current standalone applications:

- `hijra-eng-onboarding`: Hugo-powered documentation and onboarding site

## Tech Stack

- **Framework**: Next.js (v15.1.6)
- **Monorepo Management**: Nx (v20.4.2)
- **Language**: TypeScript (v5.4.2)
- **Styling**: Tailwind CSS (v4.0.5)
- **Python Formatting**: Black
- **Node Version Management**: Volta (Node 20.17.0, npm 11.1.0)
- **Testing**:
  - Unit Testing: Jest (v29.7.0)
  - E2E Testing: Playwright
- **Code Formatting**: Prettier (v3.4.2)
- **Git Hooks**: Husky (v9.1.7)
- **Documentation**: Hugo (for hijra-eng-onboarding)

## Getting Started

### Prerequisites

- Node.js (version 20.17.0 or later)
- npm (version 11.1.0 or later)
- Nx CLI (v20.4.2)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/wahidyankf/hijra-eng-onboarding.git
   cd hijra-eng-onboarding
   ```

2. Install dependencies
   ```bash
   npm install
   ```

### Development

#### Monorepo Applications

- Start the main application:

  ```bash
  npm run next-hello:dev
  ```

- Build for production:
  ```bash
  npm run next-hello:build
  ```

#### Standalone Applications

- Start the hijra-eng-onboarding documentation site:

  ```bash
  npm run hijra-eng-onboarding:dev
  ```

- Build the hijra-eng-onboarding documentation site:
  ```bash
  npm run hijra-eng-onboarding:build
  ```

## Testing

- Run all tests (including standalone and monorepo applications):

  ```bash
  npm run test:all
  ```

- Run standalone application tests:
  ```bash
  npm run test:all:standalone
  ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Git Hooks

The project uses Husky for Git hooks with automated setup:

```bash
npm run prepare
```

Hooks include:

- `pre-commit`: Runs lint-staged (Prettier for JS/TS, Black for Python)
- `commit-msg`: Validates commit messages
- `pre-push`: Runs tests and builds affected projects

The prepare script ensures all hooks are executable.

## Project Health Checks

The project includes automated checks to ensure proper setup:

### Doctor Script

```bash
npm run doctor
```

Checks:

- Required tools (nvm, black)
- Node version matches .nvmrc

### Pre-install Checks

Automatically runs during `npm install` to verify:

- Correct Node version
- Required tools are installed

## Recent Changes

- Added `hijra-eng-onboarding`: A Hugo-powered documentation site with the Hextra theme
- Implemented custom styling for cleaner UI, including hidden scrollbars
- Updated to Next.js 15.1.6 and Nx 20.4.2
- Migrated to Volta for Node version management (Node 20.17.0, npm 11.1.0)
- Simplified project structure by focusing on the hijra-eng-onboarding documentation

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Wahid Yankfi

Project Link: [https://github.com/wahidyankf/hijra-eng-onboarding](https://github.com/wahidyankf/hijra-eng-onboarding)
