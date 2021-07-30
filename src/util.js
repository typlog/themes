export function genImageURL (src, repo) {
  if (/https:\/\//.test(src)) {
    return src
  }
  return `https://cdn.jsdelivr.net/gh/${repo}/${src}`
}
