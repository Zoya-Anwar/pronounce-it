import { Card, CardContent } from "./ui/card";

const Levels = () => {
  const levels = ["Beginner", "Intermediate", "Advanced"];

  return (
    <>
      {levels.map((item) => {
        {
          return (
            <Card className="m-2">
              <CardContent className="font-bold p-2 m-2 w-55">
                {item}
              </CardContent>
            </Card>
          );
        }
      })}
    </>
  );
};

export default Levels;
