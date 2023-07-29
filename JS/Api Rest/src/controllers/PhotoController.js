import multer from 'multer';
import multerConfig from '../config/multerConfig';

import Photo from '../models/Photo';

const upload = multer(multerConfig).single('file');


class PhotoController {
  store(req, res) {
    return upload(req, res, async e => {
      if (e) {
        return res.status(400).json({
          erros: [e.code],
        });
      };

      const { originalname, filename } = req.file;
      const photo = await Photo.create({ originalname, filename })

      res.json(photo);
    });
  };
};

export default new PhotoController();
