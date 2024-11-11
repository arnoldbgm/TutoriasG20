import { IoCartOutline } from "react-icons/io5";

const page = () => {
   return (
      <div className="p-6">
         {/* Imagen */}
         <div className='overflow-hidden rounded-lg h-[438px] '>
            <img src="https://wallpapers.com/images/featured/imagenes-de-stitch-fespvm1y5taxnzl7.jpg" alt="" className='object-cover w-full h-full' />
         </div>
         {/* Title */}
         <div className="flex mt-6 justify-between">
            <div>
               <h2 className="text-3xl font-semibold">Title</h2>
               <h6 className="font-light mt-1">⭐ 5.0</h6>
            </div>
            <div className="flex items-center gap-2">
               <button type="button" className="w-7 h-7 flex items-center justify-center text-white text-sm font-bold bg-gray-800 rounded-full">-</button>
               <p className="text-2xl">1</p>
               <button type="button" className="w-7 h-7 flex items-center justify-center text-white text-sm font-bold bg-gray-800 rounded-full" >+</button>
            </div>
         </div>
         <div className="mt-4">
            <p className="line-clamp-3 overflow-hidden">Its simple and elegant shape makes it perfect for those of you who like you who want minimalist clothes</p>
         </div>
         <hr className="my-4" />
         {/* Opciones */}
         <div className="flex justify-between">
            <div>
               <h2 className="text-sm font-semibold">Choose Size</h2>
               <div className="flex flex-wrap mt-2 gap-2">
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-black text-sm border border-gray-800 rounded-full">S</button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-black text-sm border border-gray-800 rounded-full">M</button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-black text-sm border border-gray-800 rounded-full">L</button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-black text-sm border border-gray-800 rounded-full">XL</button>
               </div>
            </div>
            <div>
               <h2 className="text-sm font-semibold">Color</h2>
               <div className="flex flex-wrap justify-center mt-2 gap-2">
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-white text-sm bg-red-500 border border-gray-300 rounded-full"></button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-white text-sm bg-blue-500 border border-gray-300 rounded-full"></button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-white text-sm bg-green-500 border border-gray-300 rounded-full"></button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-white text-sm bg-yellow-500 border border-gray-300 rounded-full"></button>
                  <button type="button" className="w-8 h-8 flex items-center justify-center text-white text-sm bg-black border border-gray-300 rounded-full"></button>
               </div>
            </div>
         </div>
         {/* Boton de compra */}
         <div className="mt-6">
            <button type="button" className="w-full h-16 flex items-center justify-center text-white text-lg font-semibold bg-gray-800 rounded-[45px]"><IoCartOutline className="w-6 h-6" /> Add to Cart | $162.29</button>
         </div>
      </div>
   )
}

export default page