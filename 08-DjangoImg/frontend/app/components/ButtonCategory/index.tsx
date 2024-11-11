const ButtonCategory: React.FC<ButtonCategoryProps> = ({ label, isSelected, onClick, imagen }) => {
   return (
      <button
         type="button"
         onClick={onClick}
         className={`min-w-9 h-8 flex items-center text-xs font-normal rounded-lg px-2 ${isSelected
               ? "text-white bg-gray-800"
               : "text-gray-900 bg-white border border-gray-300"
            }`}
      >
         <img src={imagen} alt={label} className="h-4 w-4 mr-2" /> 
         {label}
      </button>
   );
}

export default ButtonCategory;
