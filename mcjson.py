from hh的小工具 import *
logs("JSON读取文件启动！",1)
import json,zipfile,os
def jsonhq(lj):
    try:
        logs("错误跟踪开始！",2)
        file=open(f".minecraft\\versions\\{lj}\\{lj}.json")
        logs(f"打开{lj}JSON",1)
        d=file.read()
        logs("正在读取JSON",1)
        file.close()
        logs("文件关闭！",1)
        data=json.loads(d)
        logs("JSON读取完成",1)
        data1=data["libraries"]
        data2=[]
        for i in data1:
            logs(i["name"]+" 库读取成功",1)
            logs("解析路径中……", 1)
            name=str(i["name"])
            name=name.split(":")
            name[0]=str(name[0]).replace(".","\\")
            logs(f"处理中（拆分路径完成）：{name}", 1)
            aabb=os.getcwd()+"\\.minecraft\\libraries\\"+name[0]+"\\"+name[1]+"\\"+name[2]+"\\"
            name=os.getcwd()+"\\.minecraft\\libraries\\"+name[0]+"\\"+name[1]+"\\"+name[2]+"\\"+name[1]+"-"+name[2]
            logs(f"处理中（拼接路径完成）：{name}", 1)
            logs(aabb)
            if "extract" in i and "natives" in i:
                logs("该库需要解压",1)
                name+="-native-windows.jar"+";"
                logs(f"处理中（补全路径完成）：{name}", 1)
                #logs(aabb+os.listdir(aabb)[0])
                """zips=zipfile.ZipFile(aabb+os.listdir(aabb)[0])
                logs(zips.namelist())
                zips.extractall(f'{str(os.getcwd())}\\.minecraft\\versions\\{lj}\\{lj}-natives')
                zips.close()
                logs("解压操作完成")"""
            else:
                name+=".jar"+";"
                logs(f"处理中（补全路径完成）：{name}", 1)
            data2.append(name)
        #print(data2)
        logs("json信息返回",1)
        #data2[-1]=data2[-1][:-1]
        #return data2
        r=""
        for i in data2:
            r+=str(i)
        logs("MinecraftJSON数据：")
        logs(data)
        mainclass=data["mainClass"]
        logs(mainclass)
        if not data["minecraftArguments"]=="":
            return mainclass,data["minecraftArguments"],False,data["assetIndex"]["id"],r
        elif data["minecraftArguments"]=="":
            data1=data["arguments"]["game"]
            data2=[]
            for i in data1:
                if '${version_type}' in i:
                    data2.append(i)
                    break
                data2.append(i)
            return mainclass,data2,True,data["assetIndex"]["id"],r
    #except:
    #    logs("程序读取时出现错误！",3)
    finally:pass
#logs(jsonhq("1.8.8"))
