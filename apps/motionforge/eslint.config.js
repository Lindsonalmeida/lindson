// Lint: JS do painel (Node 15 do CEP 11 + Chromium 88) e ExtendScript (ES3).
const globals = require("globals");
module.exports = [
  { ignores: ["**/CSInterface.js", "**/node_modules/**", "dist/**"] },
  {
    files: ["com.motionforge.panel/js/**/*.js", "com.motionforge.panel/tests/**/*.js"],
    languageOptions: { ecmaVersion: 2020, sourceType: "commonjs", globals: { ...globals.node, ...globals.browser } },
    rules: { "no-unused-vars": ["error", { args: "none", caughtErrors: "none" }], "no-undef": "error", "prefer-const": "warn", eqeqeq: ["error", "smart"], "no-var": "error" },
  },
  {
    files: ["com.motionforge.panel/jsx/**/*.jsx"],
    languageOptions: {
      ecmaVersion: 3, sourceType: "script",
      globals: { app: "readonly", File: "readonly", Folder: "readonly", CompItem: "readonly", FolderItem: "readonly", FootageItem: "readonly", SolidSource: "readonly", TextLayer: "readonly", ShapeLayer: "readonly", ImportOptions: "readonly", AlphaMode: "readonly", $: "readonly" },
    },
    rules: { "no-undef": "error", "no-unused-vars": ["error", { vars: "local", args: "none", caughtErrors: "none" }] },
  },
];
