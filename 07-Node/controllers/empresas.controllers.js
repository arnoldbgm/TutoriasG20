import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

// Hagamos la insecion de data
// req = request
// res = response
export const postEmpresa = async (req, res) => {
   try {
      const { nombre, ruc, direccion, telefono, correo_electronico, habilitado } = req.body;

      const empresaRes = await prisma.empresas.create({
         data: {
            nombre,
            ruc,
            direccion,
            telefono,
            correo_electronico,
            habilitado: habilitado !== undefined ? habilitado : true
         },
      });

      return res.json({
         msg: "Se creó la empresa correctamente",
         data: empresaRes
      });
   } catch (error) {
      console.error(error);
      return res.status(500).json({ msg: "Error al crear la empresa", error });
   }
};