import { useRouter } from "next/navigation";
import { Card, CardContent } from "./ui/card";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import z from "zod";
import { usePostLevelMutation } from "@/hooks/mutations/use-post-level-mutation";
import { useToast } from "./ui/use-toast";

const Levels = () => {
  const router = useRouter();
  const { toast } = useToast();
  const levels = ["🥔 Beginner", "🤺 Intermediate", "🏆 Advanced"];

  const levelmap = {
    "🥔 Beginner": "beginner",
    "🤺 Intermediate": "intermediate",
    "🏆 Advanced": "advanced",
  };

  const form = useForm({
    resolver: zodResolver(
      z.object({
        level: z.string(),
      })
    ),
  });

  const levelMutation = usePostLevelMutation({
    onSuccess: () => {
      console.log("success");
      router.push("/home");
    },
  });

  // const handleSubmit;

  return (
    <Card className="col space-y-2 ">
      {levels.map((item) => {
        {
          return (
            <Card className="m-2">
              <CardContent className="font-bold w-55 text-3xl text-center align-center">
                {item}
              </CardContent>
            </Card>
          );
        }
      })}
    </Card>
  );
};

export default Levels;
