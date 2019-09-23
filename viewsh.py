import logging
from google.cloud.vision import types
from google.cloud import vision

class Sunhacks:
    @staticmethod
    def localize_byte_input(byt):
        #print('inside vision.localize_byte_input')
        
        logging.info('inside yeah') 
        client = vision.ImageAnnotatorClient()

        # with io.open(path, 'rb') as image_file:
        # content = image_file.read()
        content = byt
        image = types.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        resArr = []
        print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            # print('\n{} (confidence: {})'.format(object_.name, object_.score))
            k = object_.name
            if k != 'Person' and k != 'Chair' and k != 'Table':
                continue
            # print('\n{} (confidence: {})'.format(object_.name, object_.score))
            # print('Normalized bounding polygon vertices: ')
            for vertex in object_.bounding_poly.normalized_vertices:
                if vertex.x <= 0.4:
                    resArr.append({'type': k, 'position': 'left'})
                elif vertex.x >= 0.7:
                    resArr.append({'type': k, 'position': 'right'})
                else:
                    resArr.append({'type': k, 'position': 'centre'})
                break

        print('*********', resArr)
        return resArr

#if __name__ == "__main__":
#    localize_objects_uri('/Users/renil.joseph/Documents/github/sunhacks/b.jpg')
