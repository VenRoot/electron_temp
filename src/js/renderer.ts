// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.

import $ from "jquery";
import {HTMLTags} from "./interfaces";

console.log(__dirname);

import {cpuUsage} from "./preload";

/** Gets a value from the backend, `preload.js`
 *
 */
const getData = (data?:string) =>
{
    return cpuUsage();
} 

console.log(getData(""));
