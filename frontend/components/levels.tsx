import { Card, CardContent } from "./ui/card";

const Levels = () => {
  const levels = ["Beginner", "Intermediate", "Advanced"];
  console.log(levels);

  return (
    <>
      {levels.forEach((element) => {
        <Card className="m-2">
          <CardContent className="font-bold p-2 m-2 w-55">
            {element}
          </CardContent>
        </Card>;
      })}
    </>
  );
};

export default Levels;
