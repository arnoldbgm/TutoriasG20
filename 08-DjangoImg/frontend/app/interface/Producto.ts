interface Producto {
   id: number;
   nombre: string;
   precio: number;
   rating: number;
   descripcion: string;
   imagen: string | null;
   categorias: number; // Llave foranea a mi tabla categorias
}
