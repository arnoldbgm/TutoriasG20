interface CardProductProps {
   nombre: string;
   imagen: string | null;
   precio: number;
   rating: number;
   descripcion: string;
   isSelected: boolean;
   onClick: () => void;
 }