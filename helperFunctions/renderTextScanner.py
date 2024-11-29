def render_text_scanner_page(scan_results):
    x=scan_results
    irrelevantImage = ''
    x1 = ''
    x2 = ''
    d1 = '' 
    da1 = ''
    maxdt = ''
    maxd = ''
    im1 = ''
    imp1 = ''
    it1 = ''
    imt1 = ''
    dt = ''
    pm = ''
    if x[0] == False:
        irrelevantImage = True
        print("Can't Indentify image properly")
        x1 = "Sorry, we couldn't analyze your image, make sure you upload only relevant images"
    else: 
        x1 = 'On the pictures you can see: ' \
            '1 - ' + x[0][0], '2 - ' + x[0][1], '3 - ' + x[0][2], '4 - ' + x[0][3], '5 - ' + x[0][4]

        result_1 = " Your results are = \n\n\n\n\n" + str(x[3])
        
        res = [eval(i) for i in x[4]]
        array_sum = sum(res)
        array_length = len(res)
        meand = int(array_sum / array_length)
        maxd = int(max(res))
        i = 0
        while i < 5:
            if maxd == res[i]:
                maxdt = x[5][i]
            i += 1

        print(meand)
        print(maxd)
        print(maxdt)

        if meand >= 70:
            da1 = "high"
        elif meand >= 20:
            da1 = "low"
        else:
            da1 = "medium"

        maxdt = maxdt
        result_2 = result_1.replace('[','',10)
        result_3 = result_2.replace(']','',10)
        result_f = result_3.replace("'",'',10)
        if "Benign keratosis-like lesions" in str(maxdt):
            analysis1 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Benign keratosis-like lesions. These lesions are non-cancerous growths that appear as small, rough patches on the skin. While they are not typically harmful, they can cause discomfort or become unsightly. To treat benign keratosis-like lesions, there are several options available. One of the most effective treatments is cryotherapy, which involves freezing the lesions with liquid nitrogen. This causes the lesions to blister and eventually fall off, leaving clear skin underneath. Another option is topical creams containing retinoids or alpha-hydroxy acids, which help to exfoliate the affected areas and encourage the growth of new skin cells. It is important to note that while benign keratosis-like lesions are usually harmless, there is a small chance that they could develop into skin cancer if left untreated. Therefore, it is recommended to monitor any changes in the size, shape, or color of the lesions and to seek medical attention if any suspicious changes occur. In addition to treatment, it is also important to protect your skin from further damage by wearing sunscreen and avoiding excessive sun exposure. "
            d1 = "Benign keratosis-like lesions: " + str(analysis1)
            imp1 = "Alex"
            im1 = "https://hips.hearstapps.com/hmg-prod/images/portrait-of-a-happy-young-doctor-in-his-clinic-royalty-free-image-1661432441.jpg?crop=0.66698xw:1xh;center,top&resize=1200:*"
            it1 = "https://medsurgeindia.com/wp-content/w3-webp/uploads/2020/04/Cataract-Surgery.jpgw3.webp"
            imt1 = "Laser surgery"
            dt = "+77718885212"
            pm = "500$"
        elif "dermatofibroma" in str(maxdt):
            analysis2 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Dermatofibroma. It is a common benign skin growth characterized by a firm, raised lesion that typically appears on the extremities. Its exact cause is not well understood, but it is believed to result from an inflammatory reaction or overgrowth of fibroblasts in the skin. Dermatofibromas are generally harmless and do not pose significant medical consequences, although they can occasionally cause itching or tenderness. Treatment is usually not necessary unless the lesion becomes symptomatic or there are concerns about its appearance. In such cases, options such as surgical excision, cryotherapy, laser therapy, corticosteroid injections, or observation may be considered. It is important to consult with a dermatologist for an accurate diagnosis and appropriate treatment recommendation."
            d1 = "dermatofibroma: " + str(analysis2)
            imp1 = "Elan"
            im1 = "https://turnkeymate.com/wp-content/uploads/2020/05/image-result-for-doctor-office-advertising.jpg"
            it1 = "https://www.medicaldevice-network.com/wp-content/uploads/sites/23/2021/02/shutterstock_544348294-1.jpg"
            imt1 = "Medicines against dermatofibroma"
            dt = "+77718885212"
            pm = "500$"
        elif "Melanocytic nevi" in str(maxdt):
            analysis3 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Melanocytic nevi. Melanocytic nevi, commonly known as moles, are benign skin growths that occur when melanocytes, the cells responsible for producing pigment, cluster together. They can appear anywhere on the body and vary in size, shape, and color. The exact cause of melanocytic nevi is not fully understood, but they are generally thought to be a result of a combination of genetic predisposition and sun exposure. While most moles are harmless, they can sometimes undergo changes or become atypical, which may indicate a risk for skin cancer. Therefore, it is important to monitor moles for any changes in size, shape, or color and seek medical evaluation if any concerning features are observed. Treatment options for melanocytic nevi include surgical removal, especially if they are atypical or pose a cosmetic concern, and regular monitoring through dermatological examinations to ensure early detection of any potential abnormalities."
            d1 = "Melanocytic nevi: " + str(analysis3)
            imp1 = "Michel"
            it1 = "https://insights.bukaty.com/hs-fs/hubfs/pills%20medication%20medicine.jpg?width=320&name=pills%20medication%20medicine.jpg"
            imt1 = "Medicines against melanocytic nevi"
            im1 = "https://cv-images.clickhole.com/originals/seudechqkp5jwupoiop3.jpg"
            dt = "+77718885212"
            pm = "500$"
        elif "Basal cell carcinoma" in str(maxdt):
            analysis4 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Basal cell carcinoma. Basal cell carcinoma (BCC) is the most common type of skin cancer that originates in the basal cells, which are found in the deepest layer of the epidermis. It is primarily caused by prolonged exposure to ultraviolet (UV) radiation from the sun or artificial sources like tanning beds. Other risk factors include fair skin, a history of sunburns, a weakened immune system, and exposure to certain chemicals. If left untreated, BCC can grow larger and invade surrounding tissues, causing disfigurement and damage to nearby structures. However, BCC rarely spreads to other parts of the body or becomes life-threatening. Various medical treatments are available for BCC, depending on its size, location, and severity. These treatments may include surgical excision, Mohs surgery (a specialized technique to remove cancerous tissue layer by layer), cryotherapy (freezing the affected area), curettage and electrodesiccation (scraping and burning the tumor), radiation therapy, and topical medications like imiquimod or fluorouracil. Regular follow-ups and sun protection measures are crucial in managing BCC effectively."
            d1 = "Basal cell carcinoma: " + str(analysis4)
            imp1 = "Danial"
            im1 = "https://www.topteny.com/wp-content/uploads/2015/02/doc6.jpg?x16372"
            it1 = "https://financialtribune.com/sites/default/files/field/image/17january/12_medicines_2.jpg"
            imt1 = "Medicines against basal cell carcinoma"
            dt = "+77718885212"
            pm = "500$"
        elif "Vascular lesions" in str(maxdt):
            analysis5 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Vascular lesions. Vascular lesions are abnormalities in the blood vessels that can occur in various parts of the body. They can be classified into two main types: vascular malformations and vascular tumors. Vascular malformations are congenital abnormalities in the formation of blood vessels, while vascular tumors are abnormal growths of blood vessels. The exact causes of vascular lesions are not fully understood, but they are believed to result from genetic factors and developmental problems during embryogenesis. The consequences of vascular lesions can vary depending on their location and size, but they can lead to symptoms such as pain, swelling, bleeding, and functional impairment. Treatment options for vascular lesions depend on the specific type and characteristics of the lesion. They can range from conservative management, such as observation and symptomatic relief, to more invasive interventions, including embolization, sclerotherapy, laser therapy, or surgical removal. The choice of treatment is individualized based on the your condition, the severity of symptoms, and the potential risks and benefits of each approach. Therefore, it is essential for you with vascular lesions to consult with a medical professional to determine the most appropriate treatment plan for their specific case."
            d1 = "Vascular lesions: " + str(analysis5)
            imp1 = "Alisher"
            im1 = "https://mayfairmortgages.com/wp-content/uploads/2016/10/0002_Best-doctors-3.jpg"
            it1 = "https://ksunite.com/pharma/pharma2.jpg"
            imt1 = "Medicines against vascular lesions"
            dt = "+77718885212"
            pm = "500$"
        elif "Actinic keratoses" in str(maxdt):
            analysis6 = "As a doctor, based on your symptoms and the appearance of the lesions, it is highly likely that you have Actinic keratoses. Actinic keratoses (AK) are rough, scaly patches that develop on the skin due to prolonged exposure to ultraviolet (UV) radiation, typically from the sun. They are considered precancerous lesions and can progress to squamous cell carcinoma if left untreated. The consequences of actinic keratoses include an increased risk of skin cancer, discomfort, and cosmetic concerns. Medical treatments for actinic keratoses include topical medications like imiquimod, fluorouracil, and diclofenac, which help to eliminate the lesions. Other options include cryotherapy (freezing the lesions), curettage (scraping off the affected areas), photodynamic therapy (using light and a photosensitizing agent to destroy abnormal cells), and laser therapy. Treatment aims to remove the existing lesions, prevent further progression, and reduce the risk of skin cancer development. It's important to consult with a dermatologist to determine the most suitable treatment approach based on individual circumstances."
            d1 = "Actinic keratoses: " + str(analysis6)
            imp1 = "Aibek"
            im1 = "https://www.westmauidoctors.com/wp-content/uploads/2015/11/bigstock-Happy-doctor-using-tablet-comp-50999882.jpg"
            it1 = "https://www.cgdev.org/sites/default/files/ollendorf-rare-drug-pricing-adobe-stock.jpeg"
            imt1 = "Medicines against actinic keratoses"
            dt = "+77718885212"
            pm = "500$"


        x2 = str(result_f)
    
    return irrelevantImage, x, x1, x2, d1, da1, im1, imp1, maxdt, it1, imt1, dt, pm