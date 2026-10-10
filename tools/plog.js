/* The graded probability scale for rare catastrophes (type 'plog'). A slider position 0–100 maps to a probability spread by
   factors of ten at the low end, where nearly every serious estimate sits: 0 = 0.1 % or less, 25 = 1 %, 50 = 10 %, 75 = 50 %, 100 = 99 % or more.
   The same anchors are in site/app.js (PLOG). CLI: node tools/plog.js pos 12.5   → slider position for 12.5 %
                                                   node tools/plog.js pct 64     → probability (%) at position 64 */
const A = [[0, 0.1], [25, 1], [50, 10], [75, 50], [100, 99]];
function toPct(s) { s = Math.max(0, Math.min(100, s)); for (let i = 1; i < A.length; i++) { const [s0, p0] = A[i - 1], [s1, p1] = A[i]; if (s <= s1) return Math.pow(10, Math.log10(p0) + ((s - s0) / (s1 - s0)) * (Math.log10(p1) - Math.log10(p0))); } return 99; }
function toPos(p) { p = Math.max(0.1, Math.min(99, p)); for (let i = 1; i < A.length; i++) { const [s0, p0] = A[i - 1], [s1, p1] = A[i]; if (p <= p1) return s0 + ((Math.log10(p) - Math.log10(p0)) / (Math.log10(p1) - Math.log10(p0))) * (s1 - s0); } return 100; }
module.exports = { A, toPct, toPos };
if (require.main === module) { const [cmd, x] = process.argv.slice(2); const v = Number(x); console.log(cmd === 'pos' ? Math.round(toPos(v)) : +toPct(v).toPrecision(2)); }
