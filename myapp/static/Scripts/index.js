const CajaProductos=document.querySelector(".CajaProductos")
const Refrescar=document.querySelector(".Refrescar")

const verProductosActualizar = async () => {
    const temporal=document.createElement("div")

    try {
        const response = await fetch("./productos");
        const data = await response.json();
        if (data.productos){for (const i in data.productos) {
            let contenedores=document.createElement("div")
            contenedores.classList.add("contenedores")
            let titulo=document.createElement("h2")
            let stock=document.createElement('h4')
            let precioFinal=document.createElement('h3')
            let producto = document.createElement("a");
            producto.textContent = `${data.productos[i].nombredeproducto} `;
            stock.textContent=`Stock: ${data.productos[i].cantidad}`
            precioFinal.textContent=`Precio: ${data.productos[i].precio}`
            producto.href = `productos/${data.productos[i].nombredeproducto}`;
            titulo.appendChild(producto)
            contenedores.appendChild(titulo)
            contenedores.appendChild(stock)
            contenedores.appendChild(precioFinal)
            temporal.appendChild(contenedores);
            
        } CajaProductos.innerHTML=temporal.innerHTML
        
    } 
        
        
    } catch (error) {
        console.log(error);
    }
};


const cargaInicial=async()=>{
	await verProductosActualizar()
}

window.addEventListener("load", async()=>{
	await cargaInicial()
    console.log("recibida")
})

Refrescar.addEventListener("click", async()=>{
	await cargaInicial()
    console.log("recibida")
})

