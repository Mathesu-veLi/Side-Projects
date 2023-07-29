import multer from 'multer';
import { extname, resolve } from 'path';

const randInt = () => Math.floor(Math.random() * 10000 + 10000)

export default {
  storage: multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, resolve('uploads'));
     },
    filename: (req, file, cb) => {
      cb(null, `${Date.now()}_${randInt()}${extname(file.originalname)}`);
     }
  })
};
