const moduleTest = require('./compiled/script_typescript_01')
//console.log(moduleTest)

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

const simpleList = [1, 2, 3, 4, 5, 6]

function filterHandler(){
    const response = simpleList.filter((item)=>{return item % 2 == 0})
    console.log(response)
}

filterHandler()