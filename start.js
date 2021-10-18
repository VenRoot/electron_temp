"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let platform = process.platform;
const child_process_1 = require("child_process");
switch (platform) {
    case "linux":
        console.log("Starting build for Linux");
        child_process_1.exec("npm run start:linux");
        break;
    case "win32":
        console.log("Starting build for Win32");
        child_process_1.exec("npm run start:windows");
        break;
}