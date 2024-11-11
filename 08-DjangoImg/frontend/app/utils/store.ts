import { create } from 'zustand';

interface Store {
    categories: Categoria[];
    selectedCategory: Categoria | null;
    setCategories: (categories: Categoria[]) => void;
    setSelectedCategory: (category: Categoria | null) => void;
}

const useStore = create<Store>((set) => ({
    categories: [],
    selectedCategory: null,
    setCategories: (categories) => set({ categories }),
    setSelectedCategory: (category) => set({ selectedCategory: category }),
}));


// Definición del estado de productos
interface ProductosStore {
    productos: Producto[];
    selectedProducto: Producto | null;
    setProductos: (productos: Producto[]) => void;
    setSelectedProducto: (producto: Producto | null) => void;
}

// Creación del store de productos
const useProductosStore = create<ProductosStore>((set) => ({
    productos: [],
    selectedProducto: null,
    setProductos: (productos) => set({ productos }),
    setSelectedProducto: (producto) => set({ selectedProducto: producto }),
}));

export { useStore, useProductosStore };
