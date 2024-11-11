"use client";

import { FaSearch } from 'react-icons/fa';
import { IoOptionsOutline } from "react-icons/io5";
import { CardComponent, ButtonCategory } from '../components';
import { useEffect } from 'react';
import { useStore, useProductosStore } from '../utils/store'; // Ajusta la ruta según tu estructura de carpetas

const ProductosPage = () => {
    const { categories, setCategories, selectedCategory, setSelectedCategory } = useStore();
    const { productos, setProductos, selectedProducto, setSelectedProducto } = useProductosStore();

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Fetch categorías
                const responseCategorias = await fetch('http://127.0.0.1:8000/api/v1/categorias/');
                if (!responseCategorias.ok) {
                    throw new Error('Network response for categories was not ok');
                }
                const categoriasResult = await responseCategorias.json();
                setCategories(categoriasResult);
                if (categoriasResult.length > 0) {
                    setSelectedCategory(categoriasResult[0]);
                }

                // Fetch productos
                const responseProductos = await fetch('http://127.0.0.1:8000/api/v1/productos/');
                if (!responseProductos.ok) {
                    throw new Error('Network response for products was not ok');
                }
                const productosResult = await responseProductos.json();
                setProductos(productosResult);
                if (productosResult.length > 0) {
                    setSelectedProducto(productosResult[0]);
                }
            } catch (error) {
                console.error('Error al obtener los datos:', error);
            }
        };
        fetchData();
    }, [setCategories, setSelectedCategory, setProductos, setSelectedProducto]);

    return (
        <div className="p-6">
            <div className="header flex items-center justify-between">
                <div className="header-name">
                    <h2 className="text-sm text-gray-600">Hello, Welcome 👋</h2>
                    <h3 className="text-lg font-bold">Albert Stevano</h3>
                </div>
                <div className="w-8 h-8 overflow-hidden rounded-full">
                    <img src="https://www.shutterstock.com/image-photo/handsome-happy-african-american-bearded-260nw-2460702995.jpg" className="object-cover w-full h-full" />
                </div>
            </div>
            <div className="content-search mt-4">
                <form>
                    <div className="flex gap-4">
                        <div className="relative w-full h-auto">
                            <div className="h-12 absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                                <FaSearch className="text-gray-400 w-5 h-4" />
                            </div>
                            <input
                                type="text"
                                id="search"
                                className="h-12 bg-white border border-gray-300 text-gray-900 text-sm rounded-lg  w-full pl-10 p-2.5"
                                placeholder="Search clothes"
                            />
                        </div>
                        <div>
                            <button type="button" className="w-full h-12 text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 "><IoOptionsOutline size={21} /></button>
                        </div>
                    </div>
                </form>
            </div>
            <div className="content-categories flex gap-4 overflow-x-auto mt-8"
                style={{
                    maxWidth: '100%',
                    scrollbarWidth: 'none',
                    overflowY: 'hidden'
                }} >
                {categories.map((category) => (
                    <ButtonCategory
                        key={category.id}
                        label={category.nombre}
                        imagen={category.imagen}
                        isSelected={selectedCategory?.id === category.id}
                        onClick={() => setSelectedCategory(category)}
                    />
                ))}
            </div>
            <div className="grid grid-cols-2 gap-4 mt-6">
                {productos.map((producto) => (
                    <CardComponent
                        key={producto.id}
                        nombre={producto.nombre}
                        imagen={producto.imagen}
                        precio={producto.precio}
                        rating={producto.rating}
                        descripcion={producto.descripcion}
                        isSelected={selectedProducto?.id === producto.id}
                        onClick={() => setSelectedProducto(producto)}
                    />
                ))}
            </div>
        </div>
    );
}

export default ProductosPage;
