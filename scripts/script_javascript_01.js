const moduleTest = require('./compiled/script_typescript_01')
console.log(moduleTest)

// async function loadModule() {
//     try {
//         const module = await import('./compiled/script_typescript_01.js');
//         console.log(
//             'Success loading module \n',
//             module
//         );
//     } catch (error) {
//         console.log('Error loading module:', error);
//     }
// }

// loadModule()