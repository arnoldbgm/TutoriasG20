// Obtener todos los posts
export const fetchPosts = async () => {
   try {
     const response = await fetch('https://6700ba024da5bd237554a55d.mockapi.io/blogs/');
     if (!response.ok) {
       throw new Error('Error al obtener los datos');
     }
     const data = await response.json();
     return data;
   } catch (error) {
     console.error('Error:', error);
     throw error;
   }
 };