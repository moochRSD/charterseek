#!/usr/bin/env sh
set -eu
rm -rf public
mkdir -p public
cp index.html methodology.html llms.txt robots.txt sitemap.xml favicon.svg og-image.svg public/
cp -R css data js operators public/
