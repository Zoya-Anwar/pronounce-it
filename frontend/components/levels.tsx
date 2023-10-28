import { Card, CardContent } from "./ui/card";

const Levels = () => {
  const levels = ["Beginner", "Intermediate", "Advanced"];

  return (
    <>
      {levels.map((item) =>{
      {
        return (<CardContent className="m-2">
          <Card className="font-bold p-2 m-2 w-55">
            {item}
          </Card>
        </CardContent>)
      }
      })
    }
    </>
  );
}

export default Levels ;
