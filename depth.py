import logging
from google.cloud.vision import types
from google.cloud import vision

def distance(x1, y1, x2, y2):
    x1=x1*100
    x2=x2*100
    y1=y1*100
    y2=y2*100
    x1 = int(round(x1))
    x2 = int(round(x2))
    y1 = int(round(y1))
    y2 = int(round(y2))
    p = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return int(round(p))

class Sunhacks:
    @staticmethod
    def localize_byte_input(byt, find="none"):
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

def checkDistance(find):
    resArr = []
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        # print('\n{} (confidence: {})'.format(object_.name, object_.score))
        k = object_.name
        if k != find:
            continue
        a =0, b = 0, c =0 , d=0, e = 0, f= 0, cnt = 0
        pos = ''
        for vertex in object_.bounding_poly.normalized_vertices:
            cnt=cnt+1
            if cnt ==1:
                if vertex.x <= 0.4:
                    pos = 'left'
                elif vertex.x >= 0.7:
                    pos = 'right'
                else:
                    pos = 'centre'
            break

#if __name__ == "__main__":
#    localize_objects_uri('/Users/renil.joseph/Documents/github/sunhacks/b.jpg')
