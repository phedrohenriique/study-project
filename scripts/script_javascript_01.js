console.log('javascript script 01')

import('./compiled/script_typescript_01.js').then((module) => {
    console.log(module.parameter)
})