import express from "express"
import {api as routerApi} from "./routes/empresa.routes.js"

// Configuracion
const app = express();
const port = 3000;


// Aqui debes de llamar a todos tus routes
app.use(`/api/v1`, routerApi)

// Ejecuccion del backend
try {
   app.listen(port, ()=> {
      console.log("Mi backend esta funcinoando 🦾🚀");
      console.log(`http://localhost:${port}/`);
   })
} catch (error) {
   console.error(error)
}
