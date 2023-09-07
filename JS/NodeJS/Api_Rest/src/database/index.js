import databaseConfig from '../config/database';
import Aluno from "../models/Aluno";
import User from "../models/User";
import Photo from "../models/Photo";

const models = [Aluno, User, Photo];
const { Sequelize } = require("sequelize-cockroachdb");

const connection = new Sequelize(process.env.DATABASE_URL);

models.forEach(model => model.init(connection));
models.forEach(model => model.associate && model.associate(connection.models));
