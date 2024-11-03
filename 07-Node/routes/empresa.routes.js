import { Router } from "express";

import { postEmpresa } from "../controllers/empresas.controllers.js"

export const api = Router()

api.post("/empresa", postEmpresa)
