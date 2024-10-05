import React, { useEffect, useState } from 'react';
import { HeaderComponent, PostComponent } from '../../components';

const Blog = () => {
  const [posts, setPosts] = useState([]); // Estado para almacenar la lista de posts

  useEffect(() => {
    // Función para obtener los posts del backend
    const fetchPosts = async () => {
      try {
        const response = await fetch('https://6700ba024da5bd237554a55d.mockapi.io/blogs'); // Cambia esto a la URL de tu API
        if (!response.ok) {
          throw new Error('Error al obtener los datos');
        }
        const data = await response.json();
        setPosts(data); 
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchPosts(); 
  }, []);

  return (
    <div>
      <HeaderComponent />
      <div className='w-full flex pl-[10%] pr-[10%] pt-9 flex-col'>
        <h2 className='text-center w-full font-bold text-4xl text-yellow-600'>Lista de Blogs</h2>
        {/* Listado de los Blogs */}
        <div className='grid grid-cols-3 gap-4 mt-9'>
          {posts.map(post => (
            <PostComponent key={post.id} post={post} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Blog;
