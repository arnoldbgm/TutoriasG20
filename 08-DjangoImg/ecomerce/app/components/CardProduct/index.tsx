
const CardProduct: React.FC<CardProductProps> = ({
   nombre,
   imagen,
   precio,
   rating,
   descripcion,
   isSelected,
   onClick,
 }) => {
   return (
     <div
       className={`content-cards ${isSelected ? 'border-2 border-gray-200 rounded-lg' : ''}`}
       onClick={onClick}
     >
       <div className="overflow-hidden rounded-lg">
         <img
           src={imagen || 'https://via.placeholder.com/150'}
           alt={nombre}
           className="object-cover w-full h-full"
         />
       </div>
       <div className="p-4">
         <h4 className="text-base font-semibold">{nombre}</h4>
         <h5 className="text-xs text-gray-500 font-light">{descripcion}</h5>
         <div className="flex justify-between mt-3">
           <h6 className="text-base font-semibold">${precio}</h6>
           <div>
             <h6 className="font-light">⭐{rating}</h6>
           </div>
         </div>
       </div>
     </div>
   );
 };
 
 export default CardProduct;