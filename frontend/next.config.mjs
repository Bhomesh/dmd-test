/** @type {import('next').NextConfig} */
const nextConfig = {
  basePath: '/temp',
  output: 'export',
  reactStrictMode: true,
  experimental: {
    serverModuleFormat: 'cjs',
  },
};

export default nextConfig;
